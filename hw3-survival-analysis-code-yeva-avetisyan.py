df = pd.read_csv('telco.csv')
df.head()

#changing churn into binary values
df['churn'] = df['churn'].map({'Yes': 1, 'No': 0})

#encoding categorical variables and turning them into dummies
encode_cols = ['region', 'marital', 'ed', 'retire', 'gender', 'voice', 'internet', 'forward', 'custcat']

survival_df = pd.get_dummies(df,
               columns=encode_cols,
               prefix=encode_cols,
               drop_first=True)

#The models only work for positive values, so we need to change the zeros in tenure column.
survival_df["tenure"] = np.where(survival_df["tenure"] == 0, 0.0000001, survival_df["tenure"])
survival_df.head()

#Building AFT models
wf = wf_aft()
lnf = lnf_aft()
llf = llf_aft()

fig, ax = plt.subplots(figsize=(10, 5))

list_labels = ["WeibullAFTFitter", "LogNormalAFTFitter", "LogLogisticAFTFitter"]
i = 0

for model in [wf, lnf, llf]:
    try:
        model.fit(survival_df, duration_col="tenure", event_col="churn")
        
        # Print summary
        print(f"Model: {list_labels[i]}")
        print(model.summary)
        print("")

        plt.plot(model.predict_survival_function(survival_df.loc[1]), label=list_labels[i])
        i += 1
    except Exception as e:
        print(f"Caught an error: {e}")
        pass

plt.legend()
plt.show()


logn = lnf_aft()
logn.fit(survival_df, duration_col='tenure', event_col='churn')

summary_df = logn.summary
coefficients = summary_df[['coef', 'exp(coef)', 'se(coef)', 'coef lower 95%', 'coef upper 95%']]

print("Coefficients:")
print(coefficients)

logn.plot()

#Calculating CLV's
pred = logn.predict_survival_function(survival_df)
pred

#keeping only 24 months
pred = pred.loc[1:12, :]
pred = pred.T
pred

#Calculating CLV for each person and adding to the new column of the dataframe

r = 12
monthly_margin = 1300

for col in range(0, len(pred.columns)):
    for row in range(0, 13):
        pred[col + 1][row + 1] = pred[col + 1][row + 1] / (1 + r / 12)**(row)

df['CLV'] = monthly_margin * pred.sum(axis = 0)
df.head(10)

clv = sns.displot(df, x = 'CLV', kind = 'kde', hue = 'marital')

clv = sns.displot(df, x = 'CLV', kind = 'kde', hue = 'ed')

clv = sns.displot(df, x = 'CLV', kind = 'kde', hue = 'gender')

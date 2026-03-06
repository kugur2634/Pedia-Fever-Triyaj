import numpy as np
import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import matplotlib.pyplot as plt


try:
    df = pd.read_excel('pedia.xlsx')

    print("Dosya basariyla okundu.")
    print(f"\nToplam veri sayisi: {len(df)}")
    print("\n", df.head())
except FileNotFoundError:
    print("Dosya Bulunamadi.")


copyler = []
for i in range(50):

    yeni_veri = df.copy()
    gurultu = np.random.uniform(-0.2, 0.2, len(yeni_veri))
    yeni_veri['Sicaklik'] = yeni_veri['Sicaklik'] + gurultu
    copyler.append(yeni_veri)

df_final = pd.concat([df] + copyler, ignore_index=True)
print(f"\nOrijinal veri sayisi: {len(df)}")
print(f"\nCogaltilmis veri sayisi: {len(df_final)}")
print("\n", df_final.head())


cat_variable = ['Olcum Yeri']
df_final = pd.get_dummies(data=df_final, prefix=cat_variable, columns=cat_variable)
print("\n", df_final.head())

features = [x for x in df_final.columns if x not in 'Durum']
print("\nOzellik Sayisi:", len(features))
x_train, x_val, y_train, y_val = train_test_split(df_final[features], df_final['Durum'], train_size=0.8, random_state=42)
print(f"\ntrain samples: {len(x_train)}")
print(f"\nvalidation samples: {len(x_val)}")
print(f"\ntarget proportion: {sum(y_train) / len(y_train):.4f}")

min_samples_split_list = [2, 10, 30, 50, 100, 200, 300, 700]
max_depth_list = [2, 4, 8, 16, 32, 64, None]
n_estimators_list = [10, 50, 100, 500]

accuracy_list_train = []
accuracy_list_val = []
for min_samples_split in min_samples_split_list:

    model = RandomForestClassifier(min_samples_split = min_samples_split, random_state = 42).fit(x_train, y_train)

    predictions_train = model.predict(x_train)
    predictions_val = model.predict(x_val)
    accuracy_train = accuracy_score(predictions_train, y_train)
    accuracy_val = accuracy_score(predictions_val, y_val)
    accuracy_list_train.append(accuracy_train)
    accuracy_list_val.append(accuracy_val)

plt.title("Train x Validation metrics")
plt.xlabel("min samples split")
plt.ylabel("accuracy")
plt.xticks(ticks = range(len(min_samples_split_list)), labels = min_samples_split_list)
plt.plot(accuracy_list_train)
plt.plot(accuracy_list_val)
plt.legend(['Train', 'Validation'])
plt.show()

accuracy_list_train = []
accuracy_list_val = []
for max_depth in max_depth_list:

    model = RandomForestClassifier(max_depth = max_depth, random_state = 42).fit(x_train, y_train)

    predictions_train = model.predict(x_train)
    predictions_val = model.predict(x_val)
    accuracy_train = accuracy_score(predictions_train, y_train)
    accuracy_val = accuracy_score(predictions_val, y_val)
    accuracy_list_train.append(accuracy_train)
    accuracy_list_val.append(accuracy_val)

plt.title("Train x Validation metrics")
plt.xlabel("max depth")
plt.ylabel("accuracy")
plt.xticks(ticks = range(len(max_depth_list)), labels = max_depth_list)
plt.plot(accuracy_list_train)
plt.plot(accuracy_list_val)
plt.legend(['Train', 'Validation'])
plt.show()

accuracy_list_train = []
accuracy_list_val = []
for n_estimators in n_estimators_list:

    model = RandomForestClassifier(n_estimators = n_estimators, random_state = 42).fit(x_train, y_train)

    predictions_train = model.predict(x_train)
    predictions_val = model.predict(x_val)
    accuracy_train = accuracy_score(predictions_train, y_train)
    accuracy_val = accuracy_score(predictions_val, y_val)
    accuracy_list_train.append(accuracy_train)
    accuracy_list_val.append(accuracy_val)

plt.title("Train x Validation metrics")
plt.xlabel("n estimators")
plt.ylabel("accuracy")
plt.xticks(ticks = range(len(n_estimators_list)), labels = n_estimators_list)
plt.plot(accuracy_list_train)
plt.plot(accuracy_list_val)
plt.legend(['Train', 'Validation'])
plt.show()


random_forest_model = RandomForestClassifier(n_estimators = 50, max_depth = 4, min_samples_split = 200).fit(x_train, y_train)

print(f"\nMetrics train:\n\tAccuracy score: {accuracy_score(random_forest_model.predict(x_train), y_train):.4f}")
print(f"Metrics test:\n\tAccuracy score: {accuracy_score(random_forest_model.predict(x_val), y_val):.4f}")


joblib.dump(random_forest_model, 'pedia_triyaj_model.pkl')
print("\n Model Basariyla Kaydedildi.")
import pandas as pd 
import matplotlib.pyplot  as plt


if __name__ == "__main__":
    df1 = pd.read_csv("./evaluation.csv")
    df2 = pd.read_csv("./src/evaluation.csv")

    df = pd.concat([df1, df2[["grade"]]], axis=1)
    

    df = df.rename(columns={
        "grade" : "grade3"
    })
    print(df)
    for i in range(len(df)):
        if df["grade3"][i] > 10:
            df["grade3"][i] = 1
    
    df["grade3"] = df["grade3"].astype(int)
    df["grade1"] = df["grade1"].astype(int)
    df["grade2"] = df["grade2"].astype(int)
    print(df["grade1"].mean())
    data = [df.grade1, df.grade2, df.grade3]

    fig1, ax1 = plt.subplots()
    ax1.set_title('The distribution of the grades from each evaluator.')
    ax1.set_xlabel('Evaluator')
    ax1.set_ylabel("Similarity score")
    ax1.boxplot(data, showmeans=True)
    plt.show()
    plt.savefig("./fig.png")
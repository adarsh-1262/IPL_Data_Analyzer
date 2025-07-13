import matplotlib.pyplot as plt

def plot_bar(data, title, xlabel, ylabel, color="skyblue"):
    data.plot(kind="bar", color=color, figsize=(10, 5))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
import os
import matplotlib.pyplot as plt 

def generate_charts(combined_df):

    os.makedirs("output",exist_ok=True)
    

    # --- Chart1: Bar Graph of Average Price in each category ---

    avg_price = combined_df.groupby('Category')["Price"].mean()

    plt.figure(figsize=(14,8))
    plt.bar(avg_price.index, avg_price.values)

    plt.title("Average Price By Category",fontsize = 24,fontweight="bold",color="#4C72B0")
    plt.xlabel("Category",fontsize=16,color="Black")
    plt.ylabel("Price (£)",fontsize=16, color="Black")

    plt.tick_params(
    axis="both",
    labelsize = 12,
    colors = "purple"
    )
    plt.xticks(rotation=30, ha="right",rotation_mode='anchor')


    plt.tight_layout()
    plt.savefig("output/avg_price.png")
    plt.close()       # close so chart 2 starts clean
    print("Chart 1 saved.")



    # --- Chart2: Bar Graph of Average Rating in each category ---

    avg_rating = combined_df.groupby('Category')["Rating"].mean()

    plt.figure(figsize=(14,8))
    plt.bar(avg_rating.index, avg_rating.values,color="skyblue")

    plt.title("Average Rating By Category",fontsize = 24,fontweight="bold",color="#4C72B0")
    plt.xlabel("Category",fontsize=16,color="Black")
    plt.ylabel("Rating",fontsize=16, color="Black")

    plt.tick_params(
    axis="both",
    labelsize = 12,
    colors = "purple"
    )
    plt.xticks(rotation=30, ha="right",rotation_mode='anchor')

    plt.ylim(0, 5.5)

    plt.axhline(
    y=5,
    color="red",
    linestyle="--",
    linewidth=2,
    label="Maximum Rating"
    )
    plt.legend()  # without this, the "Maximum Rating" label is never shown


    plt.tight_layout()
    plt.savefig("output/avg_rating.png")
    plt.close()
    print("Chart 2 saved.")


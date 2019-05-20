#%%

import os
import pandas as pd

data_folder = os.path.join(os.getcwd(), "数据分析\DataAnalysis\Ch4\data", "ml-100k")
# print(data_folder)

# print(os.getcwd())
ratings_filename = os.path.join(data_folder, "u.data")

# 没有表头 数据间隔使用制表符分隔
all_ratings = pd.read_csv(ratings_filename, delimiter="\t", header=None, names=["UserID", "MoiveID", "Rating", "Datetime"])

all_ratings["Datetime"] = pd.to_datetime(all_ratings["Datetime"], unit="s")

all_ratings[:5]

all_ratings["Favorable"] = all_ratings["Rating"] > 3

all_ratings[10:15]

# isin 筛选200行数据
ratings = all_ratings[all_ratings["UserID"].isin(range(200))]

ratings[:5]

favorable_ratings = ratings[ratings["Favorable"]]

favorable_ratings[:5]

favorable_reviews_by_users = dict((k, frozenset(v.values))
                                  for k, v in favorable_ratings.groupby("UserID")["MoiveID"])

favorable_reviews_by_users
# favorable_ratings[:5]

# for k, v in favorable_ratings.groupby("UserID")["MoiveID"]:
#     print(k + v)

num_favorable_by_movie = ratings[["MoiveID", "Favorable"]].groupby("MoiveID").sum()

# num_favorable_by_movie

num_favorable_by_movie.sort_values("Favorable", ascending=False)[:5]


frequent_itemsets = {}
min_support = 50

frequent_itemsets[1] = dict((frozenset((movie_id,)), row["Favorable"]) for movie_id, row in num_favorable_by_movie.iterrows() if row["Favorable"] > min_support)

frequent_itemsets[1]


from collections import defaultdict

def find_frequent_itemsets(favorable_reviews_by_users, k_l_itemsets, min_support):
    counts = defaultdict(int)
    for user, reviews in favorable_reviews_by_users.items():
        for itemset in k_l_itemsets:
            if itemset.issubset(reviews):
                for other_reviewed_movie in reviews - itemset:
                    current_superset = itemset | frozenset(
                        (other_reviewed_movie,))
                    counts[current_superset] += 1
    return dict([(itemset, frequency) for itemset, frequency in counts.items() if frequency >= min_support])

import sys

print("There are {} movies with more than {} favorable reviews".format(len(frequent_itemsets[1]), min_support))
sys.stdout.flush()
for k in range(2, 20):
    # Generate candidates of length k, using the frequent itemsets of length k-1
    # Only store the frequent itemsets
    cur_frequent_itemsets = find_frequent_itemsets(favorable_reviews_by_users, frequent_itemsets[k-1],
                                                   min_support)
    if len(cur_frequent_itemsets) == 0:
        print("Did not find any frequent itemsets of length {}".format(k))
        sys.stdout.flush()
        break
    else:
        print(cur_frequent_itemsets)
        print("I found {} frequent itemsets of length {}".format(
            len(cur_frequent_itemsets), k))
        #print(cur_frequent_itemsets)
        sys.stdout.flush()
        frequent_itemsets[k] = cur_frequent_itemsets


del frequent_itemsets[1]
    
# Now we create the association rules. First, they are candidates until the confidence has been tested
candidate_rules = []
for itemset_length, itemset_counts in frequent_itemsets.items():
    for itemset in itemset_counts.keys():
        for conclusion in itemset:
            premise = itemset - set((conclusion,))
            candidate_rules.append((premise, conclusion))
print("There are {} candidate rules".format(len(candidate_rules)))

print(candidate_rules[:5])

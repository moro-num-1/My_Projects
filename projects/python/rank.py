rank = "600lo"
xp = 0
tier = "Silver" if int(rank[0 : 3]) >= 500 else "Bronze"
xp += 10 if tier == "Bronze" else 20
print(tier)
print(xp, "xp")
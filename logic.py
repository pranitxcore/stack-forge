import pandas as pd
df=pd.read_excel("C:\\dev\\EVOLV\\evolv\\app\\StackForgeM.xlsx")
# print(df.columns)
interest_map={
    "web":"Web Dev",
    "website":"Web Dev",
    "site":"Web Dev",
    "web development":"Web Dev",
    "website development":"Web Dev",
    "data management":"Data Science",
    "data":"Data Science",
    "ai":"AI",
    "artificial intelligence":"AI",
    "machine learning":"AI",
    "ai/ml":"AI",
    "app":"App Dev",
    "application":"App Dev",
}
goal_map={
    "freelance":"Freelancing",
    "business":"Startup",
    "job":"Job"
}
exp_map={
    "new":"Beginner",
    "basic":"Beginner",
    "just started":"Beginner",
    "no experience":"Beginner",
    "mid":"Intermediate",
    "intermediate":"Intermediate",
    "medium":"Intermediate"
}

def normalize_input(user_input,mapping):
    return mapping.get(user_input.lower(),user_input)

def get_stack(interest, goal, experience):
    interest = normalize_input(interest, interest_map)
    goal = normalize_input(goal, goal_map)
    experience = normalize_input(experience, exp_map)

    result = df[
        (df["Interest"] == interest) &
        (df["Goal"] == goal) &
        (df["Experience"] == experience)
    ]

    if result.empty:
        return ["No match found"]

    tools = result.iloc[0, 3:].dropna().tolist()
    # 🔥 CRITICAL FIX
    if len(tools) == 1 and isinstance(tools[0], str):
        tools = tools[0].split(", ")
    return tools

from google import google

# https://github.com/abenassi/Google-Search-API
# To Install:  pip install git+https://github.com/abenassi/Google-Search-API
# Tp Upgrade: pip install git+https://github.com/abenassi/Google-Search-API --upgrade


for result in google.search("hello", 3):
    print(result.name)
    print(result.link)
    print(result.description) 
    print("\n")

# num_page = 3
# search_results = google.search("This is my query", num_page)


# for result in google.search("js", 3):
#     print(result.name)
#     print(result.link)
#     print(result.description) 
#     print("page: ", result.page)
#     print("index: ", result.index)
#     print("number of result found: ", result.number_of_results)
#     print("thumb: ", result.thumb)
#     print("\n\n")
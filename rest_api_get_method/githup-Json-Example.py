import  requests

url="https://api.github.com/users/celalaygar"
data = requests.get(url);
if(data) :
    print("login        : "+data.json()["login"])
    print("id           : ",data.json()["id"])
    print("name         : "+data.json()["name"])
    print("location     : "+data.json()["location"])
    print("followers    : ",data.json()["followers"])
    print("html_url     : "+data.json()["html_url"])
    print("public_repos : ",data.json()["public_repos"])
else :
    print("message      :"+data.json()["message"])
print("------------------------------------REPOS------------------------------------------------")
url += "/repos"
repo_array = requests.get(url);
if(repo_array):
    for repo in repo_array.json() :
        print("name             :"+repo["name"])
        print("full_name        :"+repo["full_name"])
        if(repo["language"]) :
            print("language         :"+repo["language"])
        if(repo["description"]) :
            print("description      :"+repo["description"])
        print("stargazers_count :",repo["stargazers_count"])
        print("owner / login    :"+repo["owner"]["login"])
        print("----------------------------")
else :
    print("message      :"+repo_array.json()["message"])




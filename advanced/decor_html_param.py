# 1/ fct décorée
# 2/ decorateur paramétrée
# 3/ décorateur implicite
# 4/ fonction de remplacement
# 5/ manipulation de la fonctin décorée
# 6/ manipulation des paramètres
# 7/ décoration de la fonctin décorée
def tags(tag):
    def deco(func):
        def wrap(content):
            return f"<{tag}>{func(content)}</{tag}>"
        return wrap
    return deco

# BONUS: gérer plusieurs balises en une fois
def tags(*tags):
    def deco(func):
        def wrap(content):
            ret = func(content)
            for tag in tags:
                ret = f"<{tag}>{ret}</{tag}>"
            return ret
        return wrap
    return deco

# @tags("strong")
# @tags("em")
@tags("strong", "em", "u")
def get_title(content):
    return content.upper()

if __name__ == "__main__":
    print(get_title("test"))
class emp:
    def __init__(self, name, domain):
        self.name=name
        self.domain=domain
    def display(self):
        print(self.name, self.domain)
if __name__ == "__main__":
    name=input("(enter your name:)")
    domain=input("(enter your city:")
    obj=emp(name, domain)
    obj.display()

class Parent:
    def properties(self):
        self.props={"gold":"2kg","bike":"passion"}
        return self.props
class Child(Parent):
    def properties(self):
        prop=super().properties()
        prop["car"]="swift"
        return prop

ch=Child()
print(ch.properties())

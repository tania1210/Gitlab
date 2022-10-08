import csv
STATUSES = {
    0: "To do",
    1: "Done"
}


class Todo:
    def __init__(self):
        self.items = []
        self.i = 0

    def fill_file(self):
        i = self.i
        self.i += 1
        with open("data.csv", "w") as file:
            writer = csv.writer(file)
            for i in self.items:
                writer.writerow(
                    [i]
                )
        self.i = 0
        pass

    def add_item(self, item, status):
        """ Method to add item """
        self.items.append({item: status})
        self.fill_file()
        self.done_item("add")
        print("reading is", dict["addElements"])
        return f"{item} successfully added with status {status}"

    def remove_item(self, index):
        self.items.pop(index)
        self.fill_file()
        self.done_item("remove")
        print("remove is", dict["removeElements"])
        pass

    def done_item(self, k):
        k = k
        if k == "add":
            dict["addElements"] = STATUSES[1]
        elif k == "remove":
            dict["removeElements"] = STATUSES[1]
        elif k == "done":
            dict["mark_item_done"] = STATUSES[1]
            print("all items are", dict["mark_item_done"])
        pass

    def show_items(self):
        return self.items

print("Enter the data:")
a = Todo()
dict = {"addElements": STATUSES[0], "removeElements": STATUSES[0], "mark_item_done": STATUSES[0]}
a.add_item(input(), 0)   # Ivan
a.add_item(input(), 1)   #Stepan
a.add_item(input(), 2)   #Oleg
a.add_item(input(), 3)   #Victor

print("Which element to remove from the file? (specify the index)")
index = int(input())
a.remove_item(index)

a.done_item("done")
print("result: ", a.show_items())
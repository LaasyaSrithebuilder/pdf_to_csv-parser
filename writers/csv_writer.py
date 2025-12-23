class CsvWriter:

    def write_transactions(self, data, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Date, Description, Currency, Amount\n")

            for row in data:
                line = ", ".join(str(col) for col in row)
                f.write(line + "\n")

    def write_customer(self, data, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Name, AccountDetails, Address\n")

            line = ", ".join([
                data.get("Name", ""),
                data.get("AccountDetails", ""),
                data.get("Address", "")
            ])
            f.write(line + "\n")

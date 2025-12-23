from interfaces import CustomerParser

class RblCustomerParser(CustomerParser):

    def parse(self, text: str) -> dict:
        lines = text.split("\n")

        name = ""
        address = []
        account = ""

        for line in lines:
            if "Sameer" in line and not name:
                name = line.strip()

            if "XXXX XXXX" in line:
                account = line.strip()

            if any(keyword in line for keyword in ["PALACE", "ROAD", "SURAT", "GJ"]):
                address.append(line.strip())

        return {
            "Name": name,
            "AccountDetails": account,
            "Address": " ".join(address)
        }

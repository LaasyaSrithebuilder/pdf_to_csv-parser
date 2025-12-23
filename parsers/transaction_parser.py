import re
from interfaces import TransactionParser

class RblTransactionParser(TransactionParser):

    DATE_REGEX = r"(?P<date>\d{2}-[A-Za-z]{3}-\d{4})"
    AMOUNT_REGEX = r"(?P<amount>[\d,]+\.\d{2}\s*(Cr|Dr)?)"

    def parse(self, text: str) -> list:
        transactions = []

        for line in text.split("\n"):
            line = line.strip()

            date_match = re.search(self.DATE_REGEX, line)
            amount_match = re.search(self.AMOUNT_REGEX, line)

            if date_match and amount_match:
                date = date_match.group("date")
                raw_amount = amount_match.group("amount").replace(",", "").strip()
                if raw_amount.endswith("Cr") or raw_amount.endswith("Dr"):
                        amount = raw_amount[:-2] + " " + raw_amount[-2:]
                else:
                     amount = raw_amount


                # Description = everything between date and amount
                start = date_match.end()
                end = amount_match.start()
                description = line[start:end].strip()

                transactions.append([
                    date,
                    description,
                    "",
                    amount
                ])

        return transactions


class Domain:
    def __init__(self, domain):
        self.domain = domain # bacteria, archaea, and eukarya

    def __str__(self) -> str:
        if self.domain in ['bacteria', 'Bacteria']:
            return f"{self.domain} - Bacteria are single-celled organisms that lack a nucleus and are typically 1-10 micrometers in size."
        elif self.domain in ['archaea', 'Archaea']:
            return f"{self.domain} - Archaea are single-celled organisms that lack a nucleus but are typically larger than bacteria."
        elif self.domain in ['eukarya', 'Eukarya']:
            return f"{self.domain} - Eukarya are organisms that have a nucleus and are typically multicellular."
        else:
            print(f" {self.domain} - There are only three domains. Bacteria, archaea, and eukarya. Please try again.")


pokus = Domain('bacteria')
print(pokus)

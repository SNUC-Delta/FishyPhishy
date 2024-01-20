import asyncio

from back.assets import internet


class PhishTank:

    def __init__(self):
        self.tar_url = r"https://github.com/mitchellkrogza/Phishing.Database/raw/master/ALL-phishing-domains.tar.gz"

    async def update_db(self):
        pass
        print("Getting binary")
        response = await internet.get_binary(self.tar_url, allow_redirects=True)
        print("Gotten binary")
        with open("phishing_domains.tar.gz", "wb") as f:
            f.write(response)
        print("Dumped")


if __name__ == "__main__":
    pt = PhishTank()
    asyncio.run(pt.update_db())

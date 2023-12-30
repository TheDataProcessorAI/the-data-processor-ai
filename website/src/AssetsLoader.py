# AssetsLoader.py
import requests as req

class AssetsLoader:
    def __init__(self):
        pass
    @staticmethod
    def load_lottieurl(url):
        r = req.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    def load_assets(self):
        lottie_urls = [
            "https://lottie.host/8feb2df2-0659-4603-8ae2-b42b40b832d4/nYJ7blGvxu.json",
            "https://lottie.host/726cc09d-84ee-4650-9eba-5b8d50bfa271/azHdrg5nqM.json",
            "https://lottie.host/29515f58-9b07-4c15-be29-a670cb4d86dd/fzsh1V2crs.json",
            "https://lottie.host/6f68c090-12b0-45b3-89ed-1a6fa2979241/9le9ajiq8W.json",
        ]

        lottie_animations = [AssetsLoader.load_lottieurl(url) for url in lottie_urls]
        return lottie_animations

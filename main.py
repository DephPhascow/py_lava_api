from dotenv import load_dotenv
from os import getenv

from py_lava_api.LavaAPI import LavaAPI

load_dotenv()

LAVA_SHOP_ID = getenv("LAVA_SHOP_ID")
LAVA_KEY_SECRET = getenv("LAVA_KEY_SECRET")
LAVA_KEY_STILL = getenv("LAVA_KEY_STILL")

lava = LavaAPI(LAVA_SHOP_ID, LAVA_KEY_SECRET, LAVA_KEY_STILL)
# balance = lava.generate_payout(1000, "adas3232", WalletTypeEnum.card_payoff, "2202202386962710")
tariffs = lava.generate_payment(200, "sdadas@3225")
# tariffs = lava.check_payout("adas3232")
# tariffs = lava.check_payment("sdadas@322")
print(tariffs)
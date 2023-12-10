from geopy.geocoders import Nominatim

def Address_Locator(latitude, longitude):
    geolocator = Nominatim(user_agent="my_geocoder")

    # 向 Nominatim 查詢地址
    location = geolocator.reverse((latitude, longitude), language="zh")

    # 提取所在國家、城市、區域和道路
    address_parts = ["country", "city", "suburb", "road"]
    result_list = [location.raw.get("address", {}).get(part, "N/A") for part in address_parts]

    return "/".join(result_list)
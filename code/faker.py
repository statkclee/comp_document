from faker import Faker
import pandas as pd

fake = Faker("ko_KR")

def create_rows_faker(num=1):
    output = [{"name"       : fake.name(),
               "email"      : fake.email(),
               "company"    : fake.company(),
               "job"        : fake.job(),
               "credit card": fake.credit_card_provider(),
               "city"       : fake.city(),
               "address"    : fake.address(),
               "ip_address" : fake.ipv4_private(),
               "profile"    : fake.profile(),
               "date_time"  : fake.date_time()} for x in range(num)]
    return output

df_faker = pd.DataFrame(create_rows_faker(100))


fake.profile()



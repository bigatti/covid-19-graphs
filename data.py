"""."""
from client import Client
from io import BytesIO
import base64
import matplotlib.pyplot as p
import datetime
import pandas
import json


class Data(object):
    """."""

    def __init__(self):
        """."""
        self._client = Client()

    def _format(self, data):
        """."""
        names = []
        values = []

        for i in data:

            date = datetime.datetime.\
                strptime(i["Date"], "%Y-%m-%dT%H:%M:%SZ")

            date = datetime.datetime.\
                strftime(date, "%Y-%m-%d")

            names.append(date)

            values.append(i["Cases"])

        return {"names": names, "values": values}

    def confirmed(self, country):
        """."""
        today = datetime.datetime.today().date()

        first = today - datetime.timedelta(days=5)

        data = self._client.country(
            country,
            "confirmed",
            first.isoformat(),
            today.isoformat())

        r = self._format(data)

        p.plot(r["names"], r["values"], "#1a75ff")

        p.title("Confirmed Cases")

        return self.converter(p_img=p)

    def deaths(self, country):
        """."""
        today = datetime.datetime.today().date()

        first = today - datetime.timedelta(days=5)
        p.cla()
        p.clf()
        data = self._client.country(
            country,
            "deaths",
            first.isoformat(),
            today.isoformat())

        r = self._format(data)

        p.plot(r["names"], r["values"], "#ff6666")

        p.title("Deaths")

        return self.converter(p_img=p)

    def recovered(self, country):
        """."""
        today = datetime.datetime.today().date()

        first = today - datetime.timedelta(days=5)

        data = self._client.country(
            country,
            "recovered",
            first.isoformat(),
            today.isoformat())

        r = self._format(data)

        p.plot(r["names"], r["values"], "#39ac39")

        p.title("Recovered")

        return self.converter(p_img=p)

    def countries_to_df(self, columns=[], head=10):
        """."""
        data = self._client.summary()

        data = json.dumps(data["Countries"])

        data = pandas.read_json(data, orient="records")

        data = data.sort_values(by=columns, ascending=False).head(head)

        return data

    def countries_confirmed(self):
        """."""
        data = self.countries_to_df(["TotalConfirmed"])

        data = data[["CountryCode", "TotalConfirmed"]].copy()

        data.columns = ["Country Code", "Total Confirmed"]

        data.plot.bar(x="Country Code", y="Total Confirmed", color="#1a75ff")

        p.title("Countries Confirmed Cases")

        p.xlabel("Country Code")

        p.ylabel("Total Confirmed (millions)")

        return self.converter(p_img=p)

    def countries_deaths(self):
        """."""
        data = self.countries_to_df(["TotalDeaths"])

        data = data[["CountryCode", "TotalDeaths"]].copy()

        data.columns = ["Country Code", "Total Deaths"]

        data.plot.bar(x="Country Code", y="Total Deaths", color="#ff3333")

        p.title("Countries Deaths")

        p.xlabel("Country Code")

        p.ylabel("Total deaths")

        return self.converter(p_img=p)

    def countries_recovered(self):
        """."""
        data = self.countries_to_df(["TotalRecovered"])

        data = data[["CountryCode", "TotalRecovered"]].copy()

        data.columns = ["Country Code", "Total Recovered"]

        data.plot.bar(x="Country Code", y="Total Recovered", color="#39ac39")

        p.title("Countries Recovered")

        p.xlabel("Country Code")

        p.ylabel("Total recovered")

        return self.converter(p_img=p)

    def converter(self, p_img):
        """."""
        figfile = BytesIO()
        p_img.savefig(figfile, format='png')
        figfile.seek(0)
        figdata_png = base64.b64encode(figfile.getvalue())
        return figdata_png.decode('utf8')

    def convert_json(self, img_base):
        """."""
        return json.dumps(
            {
                "base64": img_base
            }
        )

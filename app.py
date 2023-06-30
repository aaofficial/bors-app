import pytse_client as tse
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def check():
    ayar = tse.Ticker("عیار")
    gohar = tse.Ticker("گوهر")
    mes = tse.Ticker("مثقال")
    tala = tse.Ticker("طلا")
    kahroba = tse.Ticker("کهربا")
    zar = tse.Ticker("زر")
    seker = tse.Ticker("", index="16255851958781005")
    sekea = tse.Ticker("", index="62180931969029505")

    try:
        mes_data = mes.get_ticker_real_time_info_response()
        gohar_data = gohar.get_ticker_real_time_info_response()
        ayar_data = ayar.get_ticker_real_time_info_response()
        tala_data = tala.get_ticker_real_time_info_response()
        kahroba_data = kahroba.get_ticker_real_time_info_response()
        zar_data = zar.get_ticker_real_time_info_response()
        seker_data = seker.get_ticker_real_time_info_response()
        sekea_data = sekea.get_ticker_real_time_info_response()
    except RuntimeError:
        return "Cannot get real-time data"

    nesbat_ms = int(seker_data.best_demand_price / mes_data.best_supply_price * 100)

    return render_template(
        "index.html",
        nesbat_ms=nesbat_ms,
        mes_data=mes_data,
        gohar_data=gohar_data,
        tala_data=tala_data,
        kahroba_data=kahroba_data,
        zar_data=zar_data,
        seker_data=seker_data,
        sekea_data=sekea_data,
        ayar_data=ayar_data,
    )

    # return f"mesghal Best Supply Price: {mesghal_dl.best_demand_price}<br>" \
    #        f"mesghal Best Demand Price: {mes_data.best_demand_price}<br>" \
    #        f"mesghal Last Price: {mes_data.last_price}<br>" \
    #        f"ayar best: {ayar_data.best_supply_price}<br>" \
    #        f"ayar demand: {ayar_data.best_demand_price}<br>" \
    #        f"ayar last: {ayar_data.last_price}"

@app.route("/nesbat")
def nesbat():
    ayar = tse.Ticker("عیار")
    gohar = tse.Ticker("گوهر")
    mes = tse.Ticker("مثقال")
    tala = tse.Ticker("طلا")
    kahroba = tse.Ticker("کهربا")
    zar = tse.Ticker("زر")
    seker = tse.Ticker("", index="16255851958781005")
    sekea = tse.Ticker("", index="62180931969029505")

    try:
        mes_data = mes.get_ticker_real_time_info_response()
        gohar_data = gohar.get_ticker_real_time_info_response()
        ayar_data = ayar.get_ticker_real_time_info_response()
        tala_data = tala.get_ticker_real_time_info_response()
        kahroba_data = kahroba.get_ticker_real_time_info_response()
        zar_data = zar.get_ticker_real_time_info_response()
        seker_data = seker.get_ticker_real_time_info_response()
        sekea_data = sekea.get_ticker_real_time_info_response()
    except RuntimeError:
        return "Cannot get real-time data"

    nesbat_ms = int(seker_data.best_demand_price / mes_data.best_supply_price * 100)

    return render_template(
        "nesbat.html",
        nesbat_ms=nesbat_ms,
        mes_data=mes_data,
        gohar_data=gohar_data,
        tala_data=tala_data,
        kahroba_data=kahroba_data,
        zar_data=zar_data,
        seker_data=seker_data,
        sekea_data=sekea_data,
        ayar_data=ayar_data,
    )

    # return f"mesghal Best Supply Price: {mesghal_dl.best_demand_price}<br>" \
    #        f"mesghal Best Demand Price: {mes_data.best_demand_price}<br>" \
    #        f"mesghal Last Price: {mes_data.last_price}<br>" \
    #        f"ayar best: {ayar_data.best_supply_price}<br>" \
    #        f"ayar demand: {ayar_data.best_demand_price}<br>" \
    #        f"ayar last: {ayar_data.last_price}"


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=80)
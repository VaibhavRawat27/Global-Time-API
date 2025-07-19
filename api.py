from flask import Flask, jsonify, request
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/globaltime', methods=['GET'])
def global_time():
    country = request.args.get('country')
    timezone = request.args.get('timezone')

    # ✅ Case 1: Country name → Return official timezones
    if country and not timezone:
        try:
            # Convert country name to uppercase ISO code
            country_name = country.strip().lower()
            country_codes = {pytz.country_names[code].lower(): code for code in pytz.country_names}

            if country_name not in country_codes:
                return jsonify({"error": "Country not found"}), 404

            country_code = country_codes[country_name]
            timezones = pytz.country_timezones.get(country_code, [])

            return jsonify({
                "country": country,
                "timezones": timezones
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # ✅ Case 2: Specific timezone → Return current time
    elif timezone:
        if timezone not in pytz.all_timezones:
            return jsonify({"error": "Invalid timezone"}), 400

        tz = pytz.timezone(timezone)
        current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

        return jsonify({
            "timezone": timezone,
            "current_time": current_time
        })

    # ✅ Case 3: No input
    else:
        return jsonify({
            "message": "Please provide either 'country' (e.g., India) or 'timezone' (e.g., Asia/Kolkata)"
        }), 400


if __name__ == '__main__':
    app.run(debug=True)

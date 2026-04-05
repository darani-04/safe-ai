from flask import Flask, render_template, request
import os
app = Flask(__name__)

# Expanded demo routes with coordinates and safety scores
routes = {
    "Tiruvallur": {
        "Chennai": {
            "paths": [
                {"coords": [[13.15, 79.95], [13.08, 80.27]], "score": 95},  # Safest
                {"coords": [[13.15, 79.95], [13.10, 80.20], [13.08, 80.27]], "score": 90}  # Alt
            ]
        },
        "Tanjore": {
            "paths": [
                {"coords": [[13.15, 79.95], [10.77, 79.84]], "score": 92},
                {"coords": [[13.15, 79.95], [11.5, 79.5], [10.77, 79.84]], "score": 88}
            ]
        }
    },
    "Nagapattinam": {
        "Chennai": {
            "paths": [
                {"coords": [[10.77, 79.84], [13.08, 80.27]], "score": 94},
                {"coords": [[10.77, 79.84], [11.5, 80.0], [13.08, 80.27]], "score": 89}
            ]
        },
        "Trichy": {
            "paths": [
                {"coords": [[10.77, 79.84], [10.82, 78.69]], "score": 91},
                {"coords": [[10.77, 79.84], [11.5, 79.5], [10.82, 78.69]], "score": 87}
            ]
        }
    },
    "Madurai": {
        "Trichy": {
            "paths": [
                {"coords": [[9.92, 78.12], [10.82, 78.69]], "score": 93},
                {"coords": [[9.92, 78.12], [10.5, 78.5], [10.82, 78.69]], "score": 88}
            ]
        },
        "Chennai": {
            "paths": [
                {"coords": [[9.92, 78.12], [13.08, 80.27]], "score": 90},
                {"coords": [[9.92, 78.12], [11.5, 79.5], [13.08, 80.27]], "score": 85}
            ]
        }
    },
    "Trichy": {
        "Madurai": {
            "paths": [
                {"coords": [[10.82, 78.69], [9.92, 78.12]], "score": 93},
                {"coords": [[10.82, 78.69], [10.5, 78.5], [9.92, 78.12]], "score": 88}
            ]
        },
        "Chennai": {
            "paths": [
                {"coords": [[10.82, 78.69], [13.08, 80.27]], "score": 91},
                {"coords": [[10.82, 78.69], [12.0, 79.5], [13.08, 80.27]], "score": 87}
            ]
        },
        "Tanjore": {
            "paths": [
                {"coords": [[10.82, 78.69], [10.77, 79.84]], "score": 92},
                {"coords": [[10.82, 78.69], [11.5, 79.5], [10.77, 79.84]], "score": 88}
            ]
        }
    },
    "Tanjore": {
        "Chennai": {
            "paths": [
                {"coords": [[10.77, 79.84], [13.08, 80.27]], "score": 90},
                {"coords": [[10.77, 79.84], [12.0, 79.5], [13.08, 80.27]], "score": 86}
            ]
        },
        "Trichy": {
            "paths": [
                {"coords": [[10.77, 79.84], [10.82, 78.69]], "score": 92},
                {"coords": [[10.77, 79.84], [11.0, 79.0], [10.82, 78.69]], "score": 88}
            ]
        }
    },
    "Viluppuram": {
        "Chennai": {
            "paths": [
                {"coords": [[11.94, 79.49], [13.08, 80.27]], "score": 91},
                {"coords": [[11.94, 79.49], [12.5, 79.8], [13.08, 80.27]], "score": 87}
            ]
        }
    }
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    start = request.form['start'].strip().title()
    end = request.form['end'].strip().title()

    if start not in routes or end not in routes[start]:
        error = "Invalid start or destination location!"
        return render_template("index.html", error=error)

    # Safest route (first path)
    safest_route = routes[start][end]["paths"][0]["coords"]
    safest_score = routes[start][end]["paths"][0]["score"]

    # Alternative routes (rest)
    alt_routes = [p["coords"] for p in routes[start][end]["paths"][1:]]
    alt_scores = [p["score"] for p in routes[start][end]["paths"][1:]]

    return render_template(
        "index.html",
        start=start,
        end=end,
        safest_route=safest_route,
        safest_score=safest_score,
        alt_routes=alt_routes,
        alt_scores=alt_scores
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
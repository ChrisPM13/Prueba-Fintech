def evaluate(application, score):
    decisions = []

    # Regla 1: ingreso mínimo
    income_ok = application.income > 8000
    decisions.append(("Ingreso mayor a 8000", income_ok))

    # Regla 2: score mínimo
    score_ok = score >= 500 and score <= 900
    decisions.append(("Score entre 500 y 900", score_ok))

    approved = all(result for _, result in decisions)

    return approved, decisions

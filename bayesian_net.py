from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Build Network

model = DiscreteBayesianNetwork([

    ("Rain","Traffic"),

    ("Traffic","Late")

])

# Rain probabilities

cpd_rain = TabularCPD(

    variable="Rain",

    variable_card=2,

    values=[

        [0.7],

        [0.3]

    ]

)

# Traffic probabilities

cpd_traffic = TabularCPD(

    variable="Traffic",

    variable_card=2,

    values=[

        [0.8,0.2],

        [0.2,0.8]

    ],

    evidence=["Rain"],

    evidence_card=[2]

)

# Late probabilities

cpd_late = TabularCPD(

    variable="Late",

    variable_card=2,

    values=[

        [0.9,0.3],

        [0.1,0.7]

    ],

    evidence=["Traffic"],

    evidence_card=[2]

)

model.add_cpds(

    cpd_rain,

    cpd_traffic,

    cpd_late

)

print()

print("MODEL VALIDITY")

print(model.check_model())

print()

infer = VariableElimination(model)

result = infer.query(

    variables=["Late"],

    evidence={"Rain":1}

)

print()

print("PROBABILITY OF BEING LATE WHEN RAIN=True")

print(result)

from pyscript import display, document

def area_foratrapezoid(e):
    document.getElementById('output').innerHTML = ""

    base1 = float(document.getElementById('base1').value)
    base2 = float(document.getElementById('base2').value)
    height = float(document.getElementById('height').value)

    area = 0.5 * (base1 + base2) * height

    display(f'The area of the trapezoid with {base1} as base one, {base2} as base 2, and height as {height} is equal to {area}.', target='output')

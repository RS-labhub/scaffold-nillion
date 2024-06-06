from nada_dsl import *


def nada_main():
    var1 = Party(name="Party1")
    var2 = Party(name="Party2")
    my_int1 = SecretInteger(Input(name="my_int1", party=var1))
    my_array_1 = Array(SecretInteger(Input(name="my_array_1", party=party1)), size=100)
    my_array_2 = Array(SecretInteger(Input(name="my_array_2", party=party2)), size=100)

    unzipped = unzip(my_array_2.zip(my_array_1))

    @nada_fn
    def add(a: SecretInteger, b: SecretInteger) -> SecretInteger:
        return a + b

    new_array = my_array_1.zip(my_array_2).map(add).reduce(add, my_int1)

    out1 = Output(unzipped, "zip.unzip.tuple", var1)
    out2 = Output(new_array, "zip.map.reduce.array", var1)

    return [out1, out2]

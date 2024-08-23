def recebe_numero():
    input_var = input('Digite um valor para a operação Matemática: \n')
    input_var = float(input_var) if input_var != 'exit' else input_var
    return input_var
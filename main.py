def main():
    """
    ##################################################
    # Complete your code here
    Use the same variables: celcius fahrenheit
    ##################################################
    """
    celcius = float(input("Temperature in Celcius: "))
    fahrenheit=((9/5)*celcius)+32
    print (f'Conversion is \t {fahrenheit:.2f}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()

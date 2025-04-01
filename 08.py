def decode_ways(s, index=0, path="", result=None):
    if result is None:
        result = []
    
    if index == len(s):
        result.append(path)
        return
    num1 = int(s[index])
        
    if 1 <= num1 <= 9:
        decode_ways(s, index + 1, path + chr(num1 + 64), result)

    if index + 1 < len(s):
        num2 = int(s[index:index + 2])
        if 10 <= num2 <= 26:
            decode_ways(s, index + 2, path + chr(num2 + 64), result)
    
    return result

k=1
while k!=0:
    encoded_message = input("enter your code")
    decoded_results = decode_ways(encoded_message)
    print("Possible Decodings:")
    for decoding in decoded_results:
        print(decoding)
    k=int(input("1:again perfor task\n0:exit"))
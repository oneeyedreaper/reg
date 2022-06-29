ques=["How do we write comments in HTML?","Among the following, which is the HTML paragraph tag?","Which tag is used to create a numbered list in HTML?","What is an operating system?","What is HTML?"]
opt=["a: </…….>\nb: <!-- -->\nc: </……/>\nd: </…….*>","a: <p>\nb: <pre>\nc: <para>\nd: <a>","a: <ol>\nb: <ul>\nc: <li>\nd: <ll>","a: interface between the hardware and application programs\nb: collection of programs that manages hardware resources\nc: system service provider to the application programs\nd: all of the mentioned","a: HTML describes the structure of a webpage\nb: HTML is the standard markup language mainly used to create web pages\nc: HTML consists of a set of elements that helps the browser how to view the content\nd:  All of the mentioned"]
ans=["bB","aA","aA","dD","dD"]
x=0
z=0
for i in range(5):
    if(x==2):
        break
    print(ques[i])
    print(opt[i])
    y=input("Enter the Correct Option (a,b,c,d) = ")
    if y in ans[i]:
        z+=1
    else:
        x+=1
print("Score = " + str(z) + "\nThanks for Playing")
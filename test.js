/* function solution(s) {
    var answer = s;
    var str = ["zero","one","two","three","four","five","six","seven","eight","nine"];

    for(idx=0; idx<str.length; idx++){
        let arr = answer.split(str[idx]);
        console.log(arr)
        answer = arr.join(idx)
        console.log(answer)
    }

    console.log(answer,"얍")
    return answer/1;
}

s = "one4seveneight"

solution(s)

 */


function solution(polynomial) {
    var answer = '';
    var split = polynomial.split(" ");
    console.log(split)
    for(let idx=0; idx<split.length; idx++){
        if(split[idx].includes("x")){
            if(split[idx].length > 1){
                split[idx] = split[idx].split("x")
                split[idx][1] = "x"
            }
            console.log(split[idx])
        };
    }
    console.log(split)
    return answer;
}

polynomial = "31x + 7 + x"
solution(polynomial)
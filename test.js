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


/* function solution(polynomial) {
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
solution(polynomial) */


/* function solution(board) {
    var rows_max = board.length - 1;
    var cols_max = board[0].length - 1;

    var dangerous_place = 0;
    var every_place = (rows_max+1) * (cols_max+1);
    
    var bomb_location = [];
    
    for(var rows=0; rows<rows_max+1; rows++){
        for(var cols=0; cols<cols_max+1; cols++){
            if(board[rows][cols] == 1){
                bomb_location.push([cols,rows]);
            };
        };
    };

    dangerous_place += bomb_location.length;

    //폭탄범위 반경 2로 칠하기
    if(bomb_location.length == every_place){
        var safety_place = 0;
    } else{
        for(var bomb=0; bomb<bomb_location.length; bomb++){
            var bomb_x = bomb_location[bomb][0];
            var bomb_y = bomb_location[bomb][1];

            // x축 칠하기
            if(bomb_x == 0){
                board[bomb_y][bomb_x+1] = 2;
            } else if(bomb_x == cols_max){
                board[bomb_y][bomb_x-1] = 2;
            } else{
                board[bomb_y][bomb_x+1] = 2;
                board[bomb_y][bomb_x-1] = 2;
            }

            // y축 칠하기
            if(bomb_y == 0){
                board[bomb_y+1][bomb_x] = 2;
            } else if(bomb_y == rows_max){
                board[bomb_y-1][bomb_x] = 2;
            } else{
                board[bomb_y+1][bomb_x] = 2;
                board[bomb_y-1][bomb_x] = 2;
            }

            // 대각선 칠하기
            if((bomb_x != 0 && bomb_x != cols_max) && bomb_y == 0){
                board[bomb_y+1][bomb_x-1] = 2;
                board[bomb_y+1][bomb_x+1] = 2;
            } else if((bomb_x != 0 && bomb_x != cols_max) && bomb_y == rows_max){
                board[bomb_y-1][bomb_x-1] = 2;
                board[bomb_y-1][bomb_x+1] = 2;
            } else if((bomb_y != 0 && bomb_y != rows_max) && bomb_x == 0){
                board[bomb_y+1][bomb_x+1] = 2;
                board[bomb_y-1][bomb_x+1] = 2;
            } else if((bomb_y != 0 && bomb_y != rows_max) && bomb_x == cols_max){
                board[bomb_y+1][bomb_x-1] = 2;
                board[bomb_y-1][bomb_x-1] = 2;
            } else if(bomb_y == 0 && bomb_x == 0){
                board[bomb_y+1][bomb_x+1] = 2;
            } else if(bomb_y == 0 && bomb_x == cols_max){
                board[bomb_y+1][bomb_x-1] = 2;
            } else if(bomb_x == cols_max && bomb_y == rows_max){
                board[bomb_y-1][bomb_x-1] = 2;
            } else if(bomb_x == 0 && bomb_y == rows_max){
                board[bomb_y-1][bomb_x+1] = 2;
            }
        }

        for(var rows=0; rows<rows_max+1; rows++){
            for(var cols=0; cols<cols_max+1; cols++){
                if(board[rows][cols] == 2){
                    dangerous_place += 1;
                }
            }
            console.log(board[rows])
        };
        var safety_place = every_place - dangerous_place;
        console.log(safety_place)
    };
}


var board = [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]];
solution(board); */



function solution(d, budget) {
    var answer = 0;
    var temp = [];
    var max_length = 0;

    d.sort((a, b) => a - b);

    if(d.length == 1){
        if(d[0] > budget){
            max_length = 0;
        } else{
            max_length = 1;
        }
    }else{
        for(var idxOfd1 = 0; idxOfd1<d.length; idxOfd1++){
            var unit = [];
            var total = 0;
            if(d[idxOfd1] <= budget){
                unit.push(d[idxOfd1]);
            }
            total += d[idxOfd1];
            for(var idxOfd2 = 0; idxOfd2<d.length; idxOfd2++){
                if(idxOfd1 != idxOfd2){
                    if(total + d[idxOfd2] <= budget){
                        unit.push(d[idxOfd2]);
                        total += d[idxOfd2]
                    }
                }
            }
            temp.push(unit);
        };
        for(var idxOftemp=0; idxOftemp<temp.length; idxOftemp++){
            if(temp[idxOftemp].length > max_length){
                max_length = temp[idxOftemp].length;
            }
        };
    };

    console.log(temp);
    console.log(max_length);

    return max_length;
}

d = [1,1,1]; 
budget = 3;

solution(d, budget)


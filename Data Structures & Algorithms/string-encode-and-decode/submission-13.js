class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let encoded = [];

        strs.forEach((str) => {
            encoded.push(str.length);
            encoded.push("$");
            encoded.push(str);
        });

        return encoded.join("");
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let res = [];
        let i = 0;
        let j = 0;

        console.log(str);

        while (i < str.length){
            j = i
            while(j < str.length && str[j] !== "$"){
                j+=1
            }
            let length = Number(str.slice(i, j));
            i = j + 1;
            res.push(str.slice(i, i + length));
            i = i + length;
        }
        
        return res;
    }
}

/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function(list1, list2) {
    let result = []
    let map = new Map()
    for (let i = 0; i < list1.length; i++) {
        map.set(list1[i], i)
    }
    let min = Infinity
    for (let i = 0; i < list2.length; i++) {
        if (map.has(list2[i])) {
            if (map.get(list2[i]) + i < min) {
                result = [list2[i]]
                min = map.get(list2[i]) + i
            } else if (map.get(list2[i]) + i === min) {
                result.push(list2[i])
			}
		}
    }
    return result
};
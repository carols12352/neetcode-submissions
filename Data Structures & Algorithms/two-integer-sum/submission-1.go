func twoSum(nums []int, target int) []int {
    res := make(map[int]int)

    for i, in := range nums {
        complement := target - in
        v, ok := res[complement]
        if ok {
            return []int{v, i}
        }
                
        res[in] = i
    }
    return []int{}
}

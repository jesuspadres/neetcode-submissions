public class Solution 
{
    public int[] TwoSum(int[] nums, int target) 
    {
        int[] retVal = new int[2];
        Dictionary<int, int> map = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++) 
        {
            int diff = target - nums[i];
           
            if (map.ContainsKey(diff)) 
            {
                retVal[0] = map[diff];
                retVal[1] = i;
                return retVal;
            } else
            {
                map.Add(nums[i], i);
            }
        }

        return null;
        
    }
}

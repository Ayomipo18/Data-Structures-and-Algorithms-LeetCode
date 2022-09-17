public class Logger {
    //where n is the size of incoming messages
    //time - O(1)
    //space - O(n)
    Dictionary<string, int> times;
    
    public Logger() {
        times = new();
    }
    
    public bool ShouldPrintMessage(int timestamp, string message) {
        if(times.ContainsKey(message)) {
            if(timestamp - times[message] >= 10) {
                times[message] = timestamp;
                return true;
            }
            return false;
        } else {
            times.Add(message, timestamp);
            return true;
        }
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * bool param_1 = obj.ShouldPrintMessage(timestamp,message);
 */
package storm.jimmy;

import storm.starter.spout.RandomSentenceSpout;
import backtype.storm.Config;
import backtype.storm.LocalCluster;
import backtype.storm.StormSubmitter;
import backtype.storm.drpc.LinearDRPCTopologyBuilder;
import backtype.storm.task.ShellBolt;
import backtype.storm.task.TopologyContext;
import backtype.storm.topology.BasicOutputCollector;
import backtype.storm.topology.IRichBolt;
import backtype.storm.topology.OutputFieldsDeclarer;
import backtype.storm.topology.TopologyBuilder;
import backtype.storm.topology.base.BaseBasicBolt;
import backtype.storm.tuple.Fields;
import backtype.storm.tuple.Tuple;
import backtype.storm.tuple.Values;
import java.util.HashMap;
import java.util.Map;

/**
 * This topology demonstrates Storm's stream groupings and multilang capabilities.
 */
public class SVMDRPCTopology {
    public static class SVMBolt extends ShellBolt implements IRichBolt {
        
        public SVMBolt() {
            super("python", "svm_bolt.py");
        }

        @Override
        public void declareOutputFields(OutputFieldsDeclarer declarer) {
            declarer.declare(new Fields("id", "result"));
        }

        @Override
        public Map<String, Object> getComponentConfiguration() {
            return null;
        }
    }  
    
    public static void main(String[] args) throws Exception {
	LinearDRPCTopologyBuilder builder = new LinearDRPCTopologyBuilder("svm");
	builder.addBolt(new SVMBolt(), 3);
        Config conf = new Config();
	conf.setNumWorkers(6);
	StormSubmitter.submitTopology("svm", conf, builder.createRemoteTopology());
    }
}

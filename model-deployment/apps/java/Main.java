import java.io.IOException;

import java.util.Map;
import java.util.HashMap;
import ai.h2o.mojos.runtime.MojoPipeline;
import ai.h2o.mojos.runtime.frame.MojoFrame;
import ai.h2o.mojos.runtime.frame.MojoFrameBuilder;
import ai.h2o.mojos.runtime.frame.MojoColumn;
import ai.h2o.mojos.runtime.frame.MojoRowBuilder;
import ai.h2o.mojos.runtime.utils.SimpleCSV;
import ai.h2o.mojos.runtime.lic.LicenseException;

public class Main {

  public static void main(String[] args) throws IOException, LicenseException {
    // Load model and csv
    MojoPipeline model = MojoPipeline.loadFrom("/Users/jmedel/Development/James/Hydraulic-System-Predictive-Maintenance/model-deployment/common/hydraulic/mojo-scoring-pipeline/mp-hydr-cool-cond-y/pipeline.mojo");

    // Get and fill the input columns
    MojoFrameBuilder frameBuilder = model.getInputFrameBuilder();
    MojoRowBuilder rowBuilder = frameBuilder.getMojoRowBuilder();

    rowBuilder.setValue("psa_bar", "155.6405792236328");
    rowBuilder.setValue("psb_bar", "104.91106414794922");
    rowBuilder.setValue("psc_bar", "0.862698495388031");
    rowBuilder.setValue("psd_bar", "0.00021100000594742596");
    rowBuilder.setValue("pse_bar", "8.370246887207031");
    rowBuilder.setValue("psf_bar", "8.327606201171875");
    rowBuilder.setValue("motor_power_watt", "2161.530029296875");
    rowBuilder.setValue("fsa_vol_flow", "2.0297765731811523");
    rowBuilder.setValue("fsb_vol_flow", "8.869428634643555");
    rowBuilder.setValue("tsa_temp", "35.32681655883789");
    rowBuilder.setValue("tsb_temp", "40.87480163574219");
    rowBuilder.setValue("tsc_temp", "38.30345153808594");
    rowBuilder.setValue("tsd_temp", "30.47344970703125");
    rowBuilder.setValue("pump_eff", "2367.347900390625");
    rowBuilder.setValue("vs_vib", "0.5243666768074036");
    rowBuilder.setValue("cool_pwr_kw", "1.3104666471481323");
    rowBuilder.setValue("eff_fact_pct", "29.127466201782227");
    frameBuilder.addRow(rowBuilder);

    // Create a frame which can be transformed by MOJO pipeline
    MojoFrame iframe = frameBuilder.toMojoFrame();

    System.out.println("iframe:");
    // System.out.println("Nrows = " + iframe.getNrows());
    // System.out.println("Ncols = " + iframe.getNcols());
    // System.out.println("Column Names = " + iframe.getColumnNames());
    // System.out.println("Column Name[0] = " + iframe.getColumnName(0));
    // System.out.println("Column Data[0] = " + iframe.getColumnData(0));

    iframe.debug();

    System.out.println("Print column values in 1st row using for loop:");

    // Use Object wrapper class for Map, it is needed for NiFi Record Reader toRecord();
    Map<String, Object> testRecordMap = new HashMap<>();

    // Used to check column type for a particular column
    // MojoColumn.Type expectedColumnType;

    for(int row_i = 0; row_i < iframe.getNrows(); row_i++)
    {
      for(int col_j = 0; col_j < iframe.getNcols(); col_j++)
      {
        // Get column name at particular index
        String key = iframe.getColumnName(col_j);
         // Get column data at particular index
         // this will be an array of whatever java type the column's type is intended to represent
        // later change float[0] to object[0], then nifi record reader will infer data type
        Object columnData = iframe.getColumnData(col_j);
        // System.out.println("iframe.getColumnType(" + col_j + ") = " + iframe.getColumnType(col_j));
        
        // doing if elseif conditions for readability instead of less lines of code
        if(iframe.getColumnType(col_j) == MojoColumn.Type.Float32) 
        {
          // Gets the MojoColumn Type enum of a column at index col_j to determine the type of array for MojoColumn
          System.out.println("iframe column type = " + iframe.getColumnType(col_j));

          float[]  columnDataArray = (float[])columnData;

                  // // storing column key, value into HashMap
          System.out.println("Storing col_j =  " + col_j + ": (key,value) into HashMap");

          System.out.println("key = " + key + " columnDataArray[" + row_i + "] = " + columnDataArray[row_i]);
          
          testRecordMap.put(key,columnDataArray[row_i]);
        }
        else
        {
          System.out.println("Mojo Column Type is not supported.");
        }

        // switch(iframe.getColumnType(col_j)) {
        //   case Float32:
        //     System.out.println("iframe column type = " + iframe.getColumnType(col_j));
        //     float[]  columnDataArray = (float[])columnData;
        //     System.out.println("Storing col_j =  " + col_j + ": (key,value) into HashMap");
        //     System.out.println("key = " + key + " columnDataArray[" + row_i + "] = " + columnDataArray[row_i]);
        //     testRecordMap.put(key,columnDataArray[row_i]);
        //     break;
        //   default:
        //     System.out.println("Mojo Column Type is not supported.");
        // }

        // do if else conditions for remaining enums Bool, Int32, Int64, Float64, Str, Time64 

      }

    }

    // Testing the print of HashMap key,value
    System.out.println("Testing the print of testRecordMap HashMap key,value:");
    for(Map.Entry<String,Object> entry: testRecordMap.entrySet()) {
      System.out.println("Key = " + entry.getKey() + ", Value = " + entry.getValue());
    }

    // Transform input frame by MOJO pipeline
    MojoFrame oframe = model.transform(iframe);
    // `MojoFrame.debug()` can be used to view the contents of a Frame
    // oframe.debug();

    for(int row_i = 0; row_i < oframe.getNrows(); row_i++)
    {
      for(int col_j = 0; col_j < oframe.getNcols(); col_j++)
      {
        // Get column name at particular index
        String key = oframe.getColumnName(col_j);
         // Get column data at particular index
         // this will be an array of whatever java type the column's type is intended to represent
        // later change float[0] to object[0], then nifi record reader will infer data type
        //Object columnData = oframe.getColumnData(col_j);
        // System.out.println("oframe.getColumnType(" + col_j + ") = " + oframe.getColumnType(col_j));
        
        System.out.println("key = " + key);

        // Gets the MojoColumn Type enum of a column at index col_j to determine the type of array for MojoColumn
        System.out.println("oframe column type = " + oframe.getColumnType(col_j));

      }

    }

    oframe.debug();

    // Output prediction as CSV
    SimpleCSV outCsv = SimpleCSV.read(oframe);
    outCsv.write(System.out);
  }
}
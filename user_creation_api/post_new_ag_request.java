import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;

public class post_new_ag_request 
{
	public static void main(String args[]) throws IOException
	{
		post_new_ag_request m = new post_new_ag_request();
		Map<String, String> map = new HashMap<String, String>();
		map.put("name", "newname");
		map.put("email", "newemail");
		map.put("agency_name", "newag");
		map.put("designation", "newdesig");
		map.put("deployment", "newdep");
		int resp = m.send_request("add", "un", "pw", map);
		System.out.println(resp);
	}
	
	public int send_request(String url, String username, String password, Map message) throws IOException 
	{
		URL obj = new URL(url);
	    HttpURLConnection conn = (HttpURLConnection) obj.openConnection();

	    String request = get_json(message);
	 
	    conn.setRequestProperty("Content-Type", "application/json");
        conn.setRequestProperty("Accept", "application/json");
	    conn.setDoOutput(true);

	    conn.setRequestMethod("POST");
		conn.setConnectTimeout(5000);
		conn.setReadTimeout(5000);

		String userpass = username + ":" + password;
	    String basicAuth = "Basic " + javax.xml.bind.DatatypeConverter.printBase64Binary(userpass.getBytes("UTF-8"));

	    conn.setRequestProperty("Authorization", basicAuth);
	    
	    OutputStreamWriter out = new OutputStreamWriter(conn.getOutputStream());

	    out.write(request);
	    out.flush();
	    out.close();
	    
	    int return_code;
	    
	    try{
	    	new InputStreamReader(conn.getInputStream());
	    	return_code = conn.getResponseCode();
	    }
		catch (Exception e){
			return_code = conn.getResponseCode();
			e.printStackTrace();
	    }

		return return_code;
	}
	
	private String get_json(Map message)
	{
		//format: "{\"name\":\"na2dd1me\", \"email\": \"2ema2i3xxl\", \"agency_name\": \"ag2na23mze\", \"designation\": \"des3xi2sssg\", \"deployment\": \"de3p!1!!\"}";
		String[] fields = {"name", "email", "agency_name", "designation", "deployment"};
		StringBuilder sb = new StringBuilder();
		sb.append("{");
		for (int i = 0; i < fields.length; i++)
		{
			sb.append("\"");
			sb.append(fields[i]);
			sb.append("\":\"");
			sb.append(message.get(fields[i]));
			sb.append("\"");
			
			if (i != fields.length-1)
				sb.append(",");
		}
		sb.append("}");
		return sb.toString();
		
	}
}

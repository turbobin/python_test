/*
 * RegexTest.java
 * 
 * Copyright 2018 Administrator <Administrator@CCB>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */

/*
 * 网页爬虫（spider）
 */
import java.io.*;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.net.*;
public class RegexTest {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		getMovie();

	}

	private static void getMovie() throws Exception {
		// TODO Auto-generated method stub
		URL url = new URL("http://www.ygdy8.com");//电影天堂网址
		URLConnection conn = url.openConnection();
		InputStream in = conn.getInputStream();
		BufferedReader bufIn = 
			new BufferedReader(new InputStreamReader(in));
		
		String regex = ">201\\d年.+</";//获取所有电影名
		Pattern p = Pattern.compile(regex);
		
		File file = new File("C:\\Users\\Administrator\\Desktop\\moviespider.txt");
		PrintWriter out = 
				new PrintWriter(new FileWriter(file),true);
		
		String line = null;
		while((line=bufIn.readLine())!=null)
		{
			Matcher m = p.matcher(line);
			while(m.find())
			{
				String str = m.group();
				String movie = str.replaceAll(">","");
				movie = movie.replaceAll("</","");
				out.println(movie);
				
				
			}
		}
		System.out.println("已获取信息。");
		
		
	}

}

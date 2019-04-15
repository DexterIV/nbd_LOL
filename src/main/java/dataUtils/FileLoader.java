package main.java.dataUtils;

import org.springframework.core.io.Resource;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;

import java.io.File;
import java.io.IOException;
import java.lang.invoke.MethodHandles;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;
import org.apache.commons.io.FilenameUtils;


public class FileLoader {
    public static Map<String, String> getJSONResources() {
        Map<String, String> files = new HashMap<>();
        try {
            ClassLoader classLoader = MethodHandles.lookup().getClass().getClassLoader();
            PathMatchingResourcePatternResolver resolver = new PathMatchingResourcePatternResolver(classLoader);

            Resource[] resources = resolver.getResources("classpath:/*.json");
            for (Resource resource : resources) {
                File file = resource.getFile();
                String fileNameWithOutExt = FilenameUtils.removeExtension(file.getName());
                files.put(fileNameWithOutExt, new String(Files.readAllBytes(Paths.get(file.getPath()))));

            }
            return files;
        }catch (IOException e)
        {
            e.printStackTrace();
        }
        return files;
    }
}

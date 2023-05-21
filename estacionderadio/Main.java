import java.util.Queue;
import java.util.Scanner;
import java.util.LinkedList;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int numberOfMusics = scanner.nextInt();
        scanner.nextLine();

        Playlist playlist = new Playlist();
        for (int i = 0; i < numberOfMusics; i++) {
            String musicData = scanner.nextLine();
            String name = musicData.substring(0, 1);
            String time = musicData.substring(1);
            playlist.addMusic(name, time);
        }

        playlist.play();
        scanner.close();

    }

}

class Music {

    private String name;
    private int time;

    public Music(String name, int time) {
        this.name = name;
        this.time = time;
    }

    public String getName() { return this.name; }

    public int getTime() { return this.time; }

}

class Playlist {

    private Queue<Music> musics;

    public Playlist() {
        this.musics = new LinkedList<>();
    }

    public void addMusic(String name, String time) {
        String[] timeSplitted = time.split(":");
        int minutes = Integer.parseInt(timeSplitted[0]);
        int seconds = Integer.parseInt(timeSplitted[1]);
        int totalSeconds = (minutes * 60) + seconds;
        this.musics.offer(new Music(name, totalSeconds));
    }

    private Queue<Music> order() {
        Queue<Music> orderedMusics = new LinkedList<>(musics);
        Queue<Music> newPlaylist = new LinkedList<>();
    
        while (!orderedMusics.isEmpty()) {
            Music currentMusic = orderedMusics.poll();
            Music optimalMusic = optimalMusic(currentMusic, orderedMusics);
            if (optimalMusic != null) {
                String concatenatedName = currentMusic.getName() + optimalMusic.getName();
                int totalDuration = currentMusic.getTime() + optimalMusic.getTime();
                Music mergedMusic = new Music(concatenatedName, totalDuration);
                newPlaylist.offer(mergedMusic);
                orderedMusics.remove(optimalMusic);
            } else {
                newPlaylist.offer(currentMusic);
            }
        }
    
        return newPlaylist;
    }

    private Music optimalMusic(Music currentMusic, Queue<Music> musics) {
        int optimalDifference = Integer.MAX_VALUE;
        Music optimalMusic = null;

        for (Music music : musics) {
            int currentDuration = currentMusic.getTime();
            int musicDuration = music.getTime();
            int difference = Math.abs(180 - (currentDuration + musicDuration));
            if (difference < optimalDifference) {
                optimalDifference = difference;
                optimalMusic = music;
            }
        }
        return optimalMusic;
    }

    public void play() {
        Queue<Music> orderedMusics = order();
        StringBuilder playlistString = new StringBuilder();

        while (!orderedMusics.isEmpty()) {
            Music music = orderedMusics.poll();
            playlistString.append(music.getName());
            if (!orderedMusics.isEmpty()) {
                playlistString.append(",");
            }
        }
        System.out.println(playlistString);
    }
}
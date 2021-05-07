using UnityEngine;
using UnityEngine.UI; 

public class Score : MonoBehaviour
{
    public static int scoreCount;
    private Text scoreText;
    
    void Start()
    {
        scoreText = GetComponent<Text>();
        scoreCount = 0;
    }

    
    void Update()
    {
        scoreText.text = "Score: " + scoreCount;        
    }
}

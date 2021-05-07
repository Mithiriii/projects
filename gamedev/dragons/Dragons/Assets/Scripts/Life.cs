using UnityEngine;
using UnityEngine.UI;

public class Life : MonoBehaviour
{
    public static int lifeCount;
    private Text lifeText;
    
    void Start()
    {
        lifeText = GetComponent<Text>();
        lifeCount = 3;   
    }

    
    void Update()
    {
        lifeText.text = "Life: " + lifeCount;
    }
}

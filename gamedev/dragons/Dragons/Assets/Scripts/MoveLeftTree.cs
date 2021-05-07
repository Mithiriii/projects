using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveLeftTree : MonoBehaviour
{
    public float Speed = 1;

    

   
    // Update is called once per frame
    void Update()
    {
        
        transform.Translate(Vector3.left * Time.deltaTime * Speed, Space.World);

        if (transform.position.x < -15)
        {
            float index = UnityEngine.Random.Range(1f, 1.8f);
            transform.position += new Vector3(30, 0, 0); // Vector3.right * 30;
            transform.localScale = new Vector3(1, index, 1); 
           
        }

    }

    private void ShowRandomSprite()
    {
        int index = UnityEngine.Random.Range(0, 3);
        int childCount = transform.childCount;

        for (int i = 0; i < childCount; i++)
        {
            Transform child = transform.GetChild(i);
            child.gameObject.SetActive(index == i);
        }
    }
}

using UnityEngine;

public class MoveUpAndDown : MonoBehaviour
{

    public float HeightVariance = 1.5f;

    // Update is called once per frame
    void Update()
    {
        transform.position += Vector3.up * Mathf.Sin(Time.time) * Time.deltaTime * HeightVariance;
    }
}
